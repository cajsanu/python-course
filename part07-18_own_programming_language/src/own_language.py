# Write your solution here

import string

def get_value_and_dest(variables, line):
    parts = line.split(' ') # ['MOV', 'B', '10'] OR ['MOV', 'B', 'A']
    dest = parts[1]
    second_arg = parts[2]
    val = variables[second_arg] if second_arg in string.ascii_uppercase else int(second_arg)
    return val, dest

def mov(variables, line):
    val, dest = get_value_and_dest(variables, line)
    variables[dest] = val
    
def add(variables, line):
    val, dest = get_value_and_dest(variables, line)
    variables[dest] += val
    
def sub(variables, line):
    val, dest = get_value_and_dest(variables, line)
    variables[dest] -= val
    
def mul(variables, line):
    val, dest = get_value_and_dest(variables, line)
    variables[dest] *= val

def tulosta(variables, line, output):
    parts = line.split(' ') # ['PRINT', '34'] OR ['PRINT', 'C']
    argument = parts[1] # '34' OR 'C'
    val = variables[argument] if argument in string.ascii_uppercase else int(argument)
    output.append(val)
    
def name_code_line(locations, line, line_idx):
    location_name = line[:-1]
    locations[location_name] = line_idx
    
def jump(locations, line):
    parts = line.split(' ') # ['JUMP', 'begin'] OR ['JUMP', 'my_location_in_code']
    dest_location = parts[1]
    return locations[dest_location]
    
def if_jump(variables, locations, line, line_idx):
    parts = line.split(' ') # ['IF', 'A', '>=', 'B', 'JUMP', 'quit']
    left_side = parts[1]
    operator = parts[2]
    right_side = parts[3]
    dest_location = parts[5]
    
    val_on_left = variables[left_side] if left_side in string.ascii_uppercase else int(left_side)
    val_on_right = variables[right_side] if right_side in string.ascii_uppercase else int(right_side)
    
    if_result = False
    
    if operator == '==':
        if_result = val_on_left == val_on_right
    elif operator == '<':
        if_result = val_on_left < val_on_right
    elif operator == '>':
        if_result = val_on_left > val_on_right
    elif operator == '<=':
        if_result = val_on_left <= val_on_right
    elif operator == '>=':
        if_result = val_on_left >= val_on_right
    elif operator == '!=':
        if_result = val_on_left != val_on_right
    
    if not if_result:
        return line_idx
    else:
        return jump(locations, f"JUMP {dest_location}")
    

def run(program):
    variables = dict.fromkeys(string.ascii_uppercase, 0)
    locations = {}
    output = []
    
    for line_idx, line in enumerate(program):
        if ':' in line:
            name_code_line(locations, line, line_idx)
        
    
    line_idx = 0
    
    while line_idx < len(program):
        line = program[line_idx]
        
        if line.startswith('MOV'):
            mov(variables, line)
        elif line.startswith('ADD'):
            add(variables, line)
        elif line.startswith('SUB'):
            sub(variables, line)
        elif line.startswith('MUL'):
            mul(variables, line)
        elif line.startswith('PRINT'):
            tulosta(variables, line, output)
        elif ':' in line:
            name_code_line(locations, line, line_idx)
        elif line.startswith('JUMP'):
            line_idx = jump(locations, line)
        elif line.startswith('IF'):
            line_idx = if_jump(variables, locations, line, line_idx)
        elif line.startswith('END'):
            break
        
        line_idx += 1
    
    return output
    
# program4 = []
# program4.append("MOV N 50")
# program4.append("PRINT 2")
# program4.append("MOV A 3")
# program4.append("begin:")
# program4.append("MOV B 2")
# program4.append("MOV Z 0")
# program4.append("test:")
# program4.append("MOV C B")
# program4.append("new:")
# program4.append("IF C == A JUMP error")
# program4.append("IF C > A JUMP over")
# program4.append("ADD C B")
# program4.append("JUMP new")
# program4.append("error:")
# program4.append("MOV Z 1")
# program4.append("JUMP over2")
# program4.append("over:")
# program4.append("ADD B 1")
# program4.append("IF B < A JUMP test")
# program4.append("over2:")
# program4.append("IF Z == 1 JUMP over3")
# program4.append("PRINT A")
# program4.append("over3:")
# program4.append("ADD A 1")
# program4.append("IF A <= N JUMP begin")
# result = run(program4)
# print(result)