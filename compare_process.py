#-*- encoding:utf-8 -*-

import time

def diff_compare(input_old, input_new, result_text):
    
    old_file = read_file(input_old)
    new_file = read_file(input_new)

    for item_id in new_file:
        # Exist item
        if item_id in old_file:
            # Changed
            if old_file[item_id] != new_file[item_id]:
                result_text.insert(
                    'end', 
                    '[ID: {0}] {1} (說明變更)\n{2}\n\n----- 分隔線 -----\n\n'.format(
                        item_id, 
                        new_file[item_id]['name'], 
                        new_file[item_id]['info']
                    )
                )

        # New Item
        else:
            result_text.insert(
                'end', 
                '[ID: {0}] {1} (新增道具)\n{2}\n\n----- 分隔線 -----\n\n'.format(
                    item_id, 
                    new_file[item_id]['name'], 
                    new_file[item_id]['info']
                )
            )

    result_text.insert('end', '執行結束。')

def read_file(file_path):
    result_dict = {}
    item_flag = 0
    info_flag = False
    for line in open(file_path, 'r', encoding='utf-8-sig').readlines():

        # Item ID
        if len(line) >= 2 and line[1] == '[':
            item_id = line[2:line.find(']')]
            result_dict[item_id] = {'name': '', 'info': ''}
            item_flag = item_id
        
        elif item_flag != 0:
            if 'identifiedDisplayName' in line:
                result_dict[item_id]['name'] = line[27:-3]
            
            elif 'identifiedDescriptionName' in line:
                if '}' in line:
                    result_dict[item_id]['info'] += line[35:-3].replace('\", \"', '\n').replace('\"', '')
                
                else:
                    info_flag = True
            
            elif info_flag:
                result_dict[item_id]['info'] += line.replace('\t', '').replace('\"', '').replace(',\n', '\n')
                if line[-2] != ',':
                    info_flag = False
                    result_dict[item_id]['info'] = result_dict[item_id]['info'][:-1]
        
        if line == '\t}\n' or line == '\t},\n':
            item_flag = 0
    
    return result_dict


            
        
    
    

def read_file_old(file_path):
    result_list = []

    insert_flag = False
    for line in open(file_path, 'r', encoding='utf-8-sig').readlines():
        if insert_flag:
            if len(line) >= 1 and line[0] == '}':
                break
            result_list.append(line.replace('\t', ''))

        else:
            if len(line) > 2 and line[1] == '[':
                insert_flag = True


                result_list.append(line.replace('\t', ''))
    
    return result_list
