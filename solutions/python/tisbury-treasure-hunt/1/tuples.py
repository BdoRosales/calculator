"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])

def compare_records(azara_record, rui_record):
    azara_record=convert_coordinate(azara_record[1])
    rui_record=convert_coordinate(rui_record[1])
    
    if azara_record[1] == rui_record[1]:
            return True
    else:
            return False
    
def create_record(azara_record, rui_record):
    
    if compare_records(azara_record,rui_record):
        return azara_record+rui_record
    else:
        return "not a match"

def clean_up(combined_record_group):
    combined_record_group=tuple(combined_record_group)       
    clean_records=[]

    
    for record in combined_record_group:
        name=record[0]
        str_coordinates=record[1]
        place=record[2]
        tuple_coordinates=record[3]
        color=record[4]

        azara_record = (name, str_coordinates)
        rui_record = (place, tuple_coordinates, color)
        real_coordinates = compare_records(azara_record, rui_record)


        if real_coordinates:
            clean_records.append((name,place,tuple_coordinates,color))
            

    final_string = '\n'.join(str(r) for r in clean_records) + '\n'

    return final_string




    
    
    