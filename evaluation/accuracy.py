"""
-------------------------------------------
This script evaluates the performance of LMMs on One-Step / Two-Step / Three-Step problems and different problem domains.
-------------------------------------------

"""

import pandas as pd
import json
import numpy as np
import os
import argparse

# Function to load knowledge structure nodes
def load_knowledge_structure_nodes(filepath):
    with open(filepath, "r") as file:
        nodes = json.load(file)
    nodes = pd.DataFrame(nodes)
    nodes['final_key'] = nodes['full node'].str.split('_').str[-1]
    nodes['root_2'] = nodes['full node'].str.split('_').str[1]
    return nodes

# Function to evaluate steps
def evaluate_steps(json, steps, nodes):
    jokers = [json[[f'joker_{i}', f'knowledge concept_{i}']] for i in range(1, steps + 1)]
    for i in range(steps):
        jokers[i] = pd.merge(jokers[i], nodes[['final_key', 'full node', 'root_2']], 
                             left_on=f'knowledge concept_{i + 1}', right_on='final_key', how='left')
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


# Function to update main results DataFrame
def update_main_results_df(nodes, main_results_df, model_name, concatenated_data, merged_2steps, merged_3steps):
    One_step_acc = "{:.2%}".format(concatenated_data['joker'].mean())
    Two_step_acc = "{:.2%}".format(merged_2steps['joker_multi'].mean())
    Three_step_acc = "{:.2%}".format(merged_3steps['joker_multi'].mean())

    new_row = {
        'Model': model_name,
        'One-step(S1)': One_step_acc,
        'Two-step(S2)': Two_step_acc,
        'Three-step(S3)': Three_step_acc
}
     # Calculate rates according to Nodes
    nodes['final_rode'] = nodes['full node'].str.split('_').str[-1]
    csv_final_score = concatenated_data.groupby('final_key')['joker'].mean()
    csv_final_score = pd.merge(nodes, csv_final_score, left_on='final_rode', right_on='final_key', how='left')

    new_row.update(csv_final_score.groupby('root2')['joker'].mean().apply(lambda x: "{:.2%}".format(x)).to_dict())
    main_results_df = main_results_df._append(new_row, ignore_index=True)

    return main_results_df

# Main function to evaluate models
def evaluate_models(model_name, output_json, knowledge_structure_nodes_path, main_results_csv_path = None):

    nodes = load_knowledge_structure_nodes(knowledge_structure_nodes_path)

    main_results_df = pd.DataFrame(columns=['Model', 'One-step(S1)', 'Two-step(S2)', 'Three-step(S3)','Understanding and Conversion of Units', 'Angles and Length',
 'Calculation of Plane Figures', 'Understanding of Plane Figures',
       'Calculation of Solid Figures', 'Understanding of Solid Figures',
       'Basic Transformations of Figures','Cutting and Combining of Figures',
 'Direction','Position', 'Route Map','Correspondence of Coordinates and Positions'])
        
    print(f"Evaluating model: {model_name}, JSON path: {output_json}")
    data = load_and_process_data(output_json)
    data_2steps = data[data['key'].str.contains('2steps')]
    data_3steps = data[data['key'].str.contains('3steps')]
    merged_2steps = process_steps_data(data_2steps, 2)
    merged_3steps = process_steps_data(data_3steps, 3)

    concatenated_data = pd.concat([evaluate_steps(merged_2steps, 2, nodes), evaluate_steps(merged_3steps, 3, nodes)], axis=0)
    main_results_df = update_main_results_df(nodes, main_results_df, model_name, concatenated_data, merged_2steps, merged_3steps)

    print(main_results_df.to_string(index = False))
    if main_results_csv_path is not None:
        main_results_df.to_csv(main_results_csv_path, index=False)
        print("Evaluation completed and results saved to CSV.")

# Argument parser for command-line execution
def parse_arguments():
    parser = argparse.ArgumentParser(description='Evaluate the performance of different LMMs on four-dimensional metrics.')
    parser.add_argument('--model_name', type=str, required=True, help='Model name.')
    parser.add_argument('--output_json', type=str, required=True, help='Output json.')
    parser.add_argument('--knowledge_structure_nodes_path', type=str, required=True, help='Path to the knowledge structure nodes JSON file.')
    parser.add_argument('--main_results_csv_path', type=str, help='Path to save the main results CSV file.')
    return parser.parse_args()

# Main entry point
if __name__ == "__main__":
    args = parse_arguments()
    evaluate_models(args.model_name, args.output_json, args.knowledge_structure_nodes_path)

# python ./evaluation/accuracy.py --model_name DeepSeek-VL-1.3B --output_json /Users/mac/Desktop/kp/test/DeepSeek-VL-1.3B.json --knowledge_structure_nodes_path ~/Desktop/测试结果/knowledge_structure_nodes.json