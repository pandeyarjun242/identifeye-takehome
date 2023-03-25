patient_list = []

class Patient:
    def __init__(self, id, name):
        self.id = id;
        self.name = name
        self.exams = []
    def add(self, exam_id):
        self.exams.append(exam_id)
    def delete(self, exam_id):
        self.exams.remove(exam_id)

def delete_exam(exam_id):
    for patient in patient_list:
        if exam_id in patient.exams:
            patient.delete(exam_id)

def delete_patient(patient_id):
    for i in range(len(patient_list)):
        if patient_list[i].id == patient_id:
            patient_list.pop(i)
            return;

def add_patient(name, id):
    for patient in patient_list:
        if patient.id == id:
            return False
    new_patient = Patient(id, name)
    patient_list.append(new_patient)
    return True

def add_exam(exam_id, patient_id):
    for patient in patient_list:
        if patient.id == patient_id and exam_id not in patient.exams:
            patient.add(exam_id)
            return True
    return False

def print_output():
    for patient in patient_list:
        print('Name: ' + patient.name + ', Id: ' + str(patient.id) + ', Exam Count: ' + str(len(patient.exams)))

def main(file_name):
    input_file = open(file_name, 'r')
    lines = input_file.readlines()
    for line in lines:
        lines_modified = line.split(' ')
        lines_modified = [l.strip('\n') for l in lines_modified]
        operation = lines_modified[0]
        type = lines_modified[1]
        if operation == 'ADD':
            if type == 'EXAM':
                patient_id = lines_modified[2]
                exam_id = lines_modified[3]
                add_exam(exam_id, patient_id)
            else:
                patient_id = lines_modified[2]
                name = ' '.join(lines_modified[3:])
                add_patient(name, patient_id)
        else:
            if type == 'EXAM':
                exam_id = lines_modified[2]
                delete_exam(exam_id)
            else:
                patient_id = lines_modified[2]
                delete_patient(patient_id)
    print_output()

if __name__ == '__main__':
    main('input.txt');
