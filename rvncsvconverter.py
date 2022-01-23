import sys
import argparse
from datetime import datetime

def format_csv(filename,payout,threshold):
    out = ["\"Date\",\"Received Quantity\",\"Received Currency\",\"Sent Quantity\",\"Sent Currency\",\"Fee Amount\",\"Fee Currency\",\"Tag\""]
    with open(filename) as file:
        for line in file.readlines()[1:]:
            out_list = []
            _,date,trans_type,tag,_,qt,curr,_= line.split(",")
            date = format_date(date)
            out_list.append(date)
            trans = format_trans(trans_type, qt.strip('"').strip('-'), curr,payout,threshold)
            out_list.extend(trans)
            out_str = ",".join(out_list)
            out.append(out_str)
    out_csv = "\n".join(out)
    with open(filename,"w") as file:
        file.writelines(out_csv)

def format_date(date):
    dt = datetime.strptime(date, '\"%Y-%m-%dT%H:%M:%S\"')
    out_date = datetime.strftime(dt, '\"%m/%d/%Y %H:%M:%S\"')
    return out_date
    
def format_trans(trans_type, qt, curr, payout, threshold):
    rec_qt,rec_curr,sent_qt,sent_curr,tag = "\"\"","\"\"","\"\"","\"\"","\"\""
    if trans_type == "\"Sent to\"":
        sent_qt = "\"" + qt + "\""
        sent_curr = curr
    elif trans_type == "\"Received with\"":
        rec_qt = "\"" + qt + "\""
        rec_curr = curr
        if abs(float(qt)-payout) < threshold:
            tag = "\"mined\""
    return [rec_qt,rec_curr,sent_qt,sent_curr,"\"\"","\"\"",tag]

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='F', type=str)
    parser.add_argument('--payout', type=int, required=True)
    parser.add_argument('--threshold', type=int, required=True)
    args = parser.parse_args()
    format_csv(sys.argv[1],args.payout,args.threshold)

if __name__ == '__main__':
    main()
