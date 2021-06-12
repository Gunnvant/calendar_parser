from ics import Calendar
import pandas as pd
import os
import click  

def read_ics(path):
    with open(path,"r",encoding="utf-8") as f:
        ics_text = f.read()
    return ics_text

def make_event_list(ics_text):
    c = Calendar(ics_text)
    return list(c.events)

def parse_event(event):
    begin = event.begin.datetime.strftime("%d-%m-%Y %H:%M:%S")
    end = event.end.datetime.strftime("%d-%m-%Y %H:%M:%S")
    name = event.name 
    duration = event.duration.seconds
    return (name, begin, end, duration)

def parse_all_events(events):
    data = [] 
    for event in events:
        data.append(parse_event(event))
    return data     

@click.command()
@click.option("--path_from", 
             prompt="Path to the ICS file", 
             help="Path to read the ICS file from")
@click.option("--path_to", 
            prompt="Path to write the csv file to", 
            help="Path to write the csv file to",
            default=".")
def main(path_from,path_to):
    headers = ['name','begin','end','duration']
    path_ics_file = os.path.abspath(path_from)
    ics_text = read_ics(path_ics_file)
    events = make_event_list(ics_text)
    data = parse_all_events(events)
    path_to = os.path.abspath(path_to)
    path_to = os.path.join(path_to,"calendar.csv")
    pd.DataFrame(data,columns=headers).to_csv(path_to,index=False)
if __name__ == "__main__":
   main()

