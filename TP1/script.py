def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(',') #string removes the /n in the last collum of the line
            data.append({
                'modalidade': parts[8],
                'idade': int(parts[5]),
                'resultado': parts[12].lower() == 'true'
            })
    return data



def calculate_percentage(entries):
    total = len(entries)
    true_count = sum(1 for entry in entries if entry['resultado'])
    false_count = total - true_count
    return (true_count / total * 100, false_count / total * 100)



def group_by_age(entries):
    age_groups = {}
    for entry in entries:
        age_group = entry['idade'] // 5 * 5
        if age_group not in age_groups:
            age_groups[age_group] = 0
        age_groups[age_group] += 1
    return age_groups


if __name__ == "__main__":
    filename = 'emd.csv'
    data = read_csv(filename)
    
    modalidades = set()
    for entry in data: modalidades.add(entry['modalidade'])
    print("Modalidades" + str(modalidades) + "\n")

    # Calculate percentage of true and false results
    true_percentage, false_percentage = calculate_percentage(data)
    print(f"Percentagem de atletas aptos: {true_percentage:.2f}%")
    print(f"Percentagem de atletas inaptos: {false_percentage:.2f}%\n")
    
    # Group entries by age
    age_groups = group_by_age(data)
    print("Distribuição de atletas por escalão etário:")
    for age_group, count in sorted(age_groups.items()):
        print(f"Idades {age_group} - {age_group + 4}: {count}")