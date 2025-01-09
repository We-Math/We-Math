"""
-------------------------------------------
Used for evaluate the performance of different LMMs on four-dimensional metrics.
Including four distinct conditions (IK, IG, CM, RM) and average final score.
Under strict and loose conditions.
-------------------------------------------

## Description of evaluation steps:
# This script evaluates the performance of different language models on a four-dimensional metrics system.
# It includes strict and loose conditions for four distinct metrics: Inadequate Knowledge (IK), 
# Inadequate Generalization (IG), Complete Mastery (CM), and Rote Memorization (RM). 
# The final score is also calculated under both strict and loose conditions.
# The script takes optional arguments for the number of models, model_name, input result JSON directory, 
# and output result CSV. It processes each model's results and calculates the evaluation metrics.
"""

import pandas as pd
import json
import numpy as np
import os
import argparse

# Function to evaluate steps
def evaluate_steps(json, steps):
    jokers = [json[[f'joker_{i}', f'knowledge concept_{i}']] for i in range(1, steps + 1)]
    for i in range(steps):
        jokers[i].rename(columns={f'joker_{i + 1}': 'joker', f'knowledge concept_{i + 1}': 'knowledge_concept'}, inplace=True)
    concatenated_steps = pd.concat(jokers, axis=0)
    return concatenated_steps

# Function to load and process JSON data
def load_and_process_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df['processed_answer'] = df['response'].str.split('Answer').str[-1].str.strip().str.replace(r'[>><<:.]', '', regex=True).str.strip()
    df['processed_answer'] = df['processed_answer'].apply(lambda x: x[0] if x and x[0] in 'ABCDEFGH' else None)
    df['joker'] = df['processed_answer'] == df['answer']
    return df

# Function to process steps data and merge results
def process_steps_data(df, steps):
    steps_data = {f'{steps}steps_{i}': df[df['key'] == f'{steps}steps_{i}'] for i in range(1, steps + 1)}
    steps_data[f'{steps}steps_multi'] = df[df['key'] == f'{steps}steps_multi']
    for key, data in steps_data.items():
        data.columns = [col + f'_{key.split("_")[-1]}' for col in data.columns]
    merged_data = steps_data[f'{steps}steps_1']
    for i in range(2, steps + 1):
        merged_data = pd.merge(merged_data, steps_data[f'{steps}steps_{i}'], left_on=f'ID_1', right_on=f'ID_{i}', how='left')
    merged_data = pd.merge(merged_data, steps_data[f'{steps}steps_multi'], left_on=f'ID_1', right_on='ID_multi', how='left')
    return merged_data

# Function to calculate evaluation metrics
def calculate_metrics(merged_2steps, merged_3steps):
    metrics = {}
    metrics['steps2_filtered_rows_1_loose'] = merged_2steps[((merged_2steps['joker_1'] == False) & (merged_2steps['joker_2'] == False)) & (merged_2steps['joker_multi'] == True)]
    metrics['steps2_filtered_rows_1_strict'] = merged_2steps[((merged_2steps['joker_1'] == False) | (merged_2steps['joker_2'] == False)) & (merged_2steps['joker_multi'] == True)]
    metrics['steps2_filtered_rows_2'] = merged_2steps[((merged_2steps['joker_1'] == True) & (merged_2steps['joker_2'] == True)) & (merged_2steps['joker_multi'] == False)]
    metrics['steps2_filtered_rows_3'] = merged_2steps[((merged_2steps['joker_1'] == False) | (merged_2steps['joker_2'] == False)) & (merged_2steps['joker_multi'] == False)]
    metrics['steps2_filtered_rows_4_loose'] = merged_2steps[((merged_2steps['joker_1'] == True) | (merged_2steps['joker_2'] == True)) & (merged_2steps['joker_multi'] == True)]
    metrics['steps2_filtered_rows_4_strict'] = merged_2steps[((merged_2steps['joker_1'] == True) & (merged_2steps['joker_2'] == True)) & (merged_2steps['joker_multi'] == True)]
    metrics['steps3_filtered_rows_1_loose'] = merged_3steps[((merged_3steps['joker_1'] == False) & (merged_3steps['joker_2'] == False) & (merged_3steps['joker_3'] == False)) & (merged_3steps['joker_multi'] == True)]
    metrics['steps3_filtered_rows_1_strict'] = merged_3steps[((merged_3steps['joker_1'] == False) | (merged_3steps['joker_2'] == False) | (merged_3steps['joker_3'] == False)) & (merged_3steps['joker_multi'] == True)]
    metrics['steps3_filtered_rows_2'] = merged_3steps[((merged_3steps['joker_1'] == True) & (merged_3steps['joker_2'] == True) & (merged_3steps['joker_3'] == True)) & (merged_3steps['joker_multi'] == False)]
    metrics['steps3_filtered_rows_3'] = merged_3steps[((merged_3steps['joker_1'] == False) | (merged_3steps['joker_2'] == False) | (merged_3steps['joker_3'] == False)) & (merged_3steps['joker_multi'] == False)]
    metrics['steps3_filtered_rows_4_loose'] = merged_3steps[((merged_3steps['joker_1'] == True) | (merged_3steps['joker_2'] == True) | (merged_3steps['joker_3'] == True)) & (merged_3steps['joker_multi'] == True)]
    metrics['steps3_filtered_rows_4_strict'] = merged_3steps[((merged_3steps['joker_1'] == True) & (merged_3steps['joker_2'] == True) & (merged_3steps['joker_3'] == True)) & (merged_3steps['joker_multi'] == True)]
    # metrics.to_csv("/Users/mac/Desktop/测试结果/error_anal/csv/gpt4o-0626.csv", index = False)
    return metrics

# Function to compute evaluation rates and final scores
def compute_final_scores(metrics, total_count):
    total_counts = {
        'InadequateGeneralization': len(metrics['steps2_filtered_rows_2']) + len(metrics['steps3_filtered_rows_2']),
        'InsufficientKnowledge': len(metrics['steps2_filtered_rows_3']) + len(metrics['steps3_filtered_rows_3']),
        'CompleteMastery_loose': len(metrics['steps2_filtered_rows_4_loose']) + len(metrics['steps3_filtered_rows_4_loose']),
        'CompleteMastery_strict': len(metrics['steps2_filtered_rows_4_strict']) + len(metrics['steps3_filtered_rows_4_strict']),
        'RoteMemorization_loose': len(metrics['steps2_filtered_rows_1_loose']) + len(metrics['steps3_filtered_rows_1_loose']),
        'RoteMemorization_strict': len(metrics['steps2_filtered_rows_1_strict']) + len(metrics['steps3_filtered_rows_1_strict'])
    }
    rates = {
        'InadequateGeneralization_rate': "{:.2%}".format(total_counts['InadequateGeneralization'] / total_count),
        'InsufficientKnowledge_rate': "{:.2%}".format(total_counts['InsufficientKnowledge'] / total_count),
        'CompleteMastery_loose_rate': "{:.2%}".format(total_counts['CompleteMastery_loose'] / total_count),
        'CompleteMastery_strict_rate': "{:.2%}".format(total_counts['CompleteMastery_strict'] / total_count),
        'RoteMemorization_loose_rate': "{:.2%}".format(total_counts['RoteMemorization_loose'] / (total_counts['CompleteMastery_loose'] + total_counts['RoteMemorization_loose'])),
        'RoteMemorization_strict_rate': "{:.2%}".format(total_counts['RoteMemorization_strict'] / (total_counts['CompleteMastery_strict'] + total_counts['RoteMemorization_strict']))
    }
    return total_counts, rates

# Function to update main results DataFrame
def update_main_results_df(main_results_df, model, total_counts, rates):

    final_score_loose = "{:.2%}".format((525 - 0.5 * total_counts['InadequateGeneralization'] - total_counts['RoteMemorization_loose'] - total_counts['InsufficientKnowledge']) / 525)
    final_score_strict = "{:.2%}".format((525 - 0.5 * total_counts['InadequateGeneralization'] - total_counts['RoteMemorization_strict'] - total_counts['InsufficientKnowledge']) / 525)

    new_row = {
        'Model': model,
        'Score (Strict)': final_score_strict,
        'InsufficientKnowledge (Strict)': f"{rates['InsufficientKnowledge_rate']} ({total_counts['InsufficientKnowledge']})",
        'InadequateGeneralization (Strict)': f"{rates['InadequateGeneralization_rate']} ({total_counts['InadequateGeneralization']})",
        'CompleteMastery (Strict)': f"{rates['CompleteMastery_strict_rate']} ({total_counts['CompleteMastery_strict']})",
        'RoteMemorization (Strict)': f"{rates['RoteMemorization_strict_rate']} ({total_counts['RoteMemorization_strict']})",

        'Score (Loose)': final_score_loose,
        'InsufficientKnowledge (Loose)': f"{rates['InsufficientKnowledge_rate']} ({total_counts['InsufficientKnowledge']})",
        'InadequateGeneralization (Loose)': f"{rates['InadequateGeneralization_rate']} ({total_counts['InadequateGeneralization']})",
        'CompleteMastery (Loose)': f"{rates['CompleteMastery_loose_rate']} ({total_counts['CompleteMastery_loose']})",
        'RoteMemorization (Loose)': f"{rates['RoteMemorization_loose_rate']} ({total_counts['RoteMemorization_loose']})"
    }
    main_results_df = main_results_df._append(new_row, ignore_index=True)
    return main_results_df

# Main function to evaluate models
def evaluate_models(model_name, output_json, main_results_csv_path = None):

    main_results_df = pd.DataFrame(columns=['Model', 'Score (Strict)', 'InsufficientKnowledge (Strict)', 'InadequateGeneralization (Strict)', 'CompleteMastery (Strict)', 'RoteMemorization (Strict)', 'Score (Loose)', 'InsufficientKnowledge (Loose)', 'InadequateGeneralization (Loose)', 'CompleteMastery (Loose)', 'RoteMemorization (Loose)'])
        
    print(f"Evaluating model: {model_name}, JSON path: {output_json}")
    data = load_and_process_data(output_json)
    data_2steps = data[data['key'].str.contains('2steps')]
    data_3steps = data[data['key'].str.contains('3steps')]
    merged_2steps = process_steps_data(data_2steps, 2)
    merged_3steps = process_steps_data(data_3steps, 3)

    metrics = calculate_metrics(merged_2steps, merged_3steps)
    total_counts, rates = compute_final_scores(metrics, total_count=525)

    main_results_df = update_main_results_df(main_results_df, model_name, total_counts, rates)

    print(main_results_df.to_string(index = False))
    if main_results_csv_path is not None:
        main_results_df.to_csv(main_results_csv_path, index=False)
        print("Evaluation completed and results saved to CSV.")

# Argument parser for command-line execution
def parse_arguments():
    parser = argparse.ArgumentParser(description='Evaluate the performance of different LMMs on four-dimensional metrics.')
    parser.add_argument('--model_name', type=str, required=True, help='Evaluation for multiple models or a single model')
    parser.add_argument('--output_json', type=str, required=True, help='Directory containing the result JSON files.')
    parser.add_argument('--main_results_csv_path', type=str, help='Path to save the main results CSV file.')
    return parser.parse_args()

# Main entry point
if __name__ == "__main__":
    args = parse_arguments()
    evaluate_models(args.model_name, args.output_json)

