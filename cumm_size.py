"""Take a text file which contains list of DBs and give the cummulative sum for each db reading the specific size field"""
"""In line number 32 just replace it with the list text file location.Extension should be .txt"""
import json
import os

def readfile(listtext):
    output_arr = []
    f = open(listtext)
    while True:
        # Get next line from file
        line = f.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        output_arr.append(line.strip())
    return output_arr

def cumm_size(output_arr):
    sum_all_instance = 0

    for db in output_arr:
        sh_cmd = os.system("aws rds describe-db-log-files --db-instance-identifier {} --filename-contains='mysql-error' --profile=dev --region=ap-southeast-1 > {}.json".format(
            db, db))
        filename = db + '.json'
        f = open(filename)
        data = json.load(f)
        tot_sum = 0
        for i in data['DescribeDBLogFiles']:
            tot_sum = tot_sum + i['Size']
        print(db, tot_sum)
        sum_all_instance=sum_all_instance+tot_sum

        if os.path.isfile(filename):
            os.remove(filename)
        else:  ## Show an error ##
            print("Error: %s file not found" % filename)
    sum_all_instance_in_gb=sum_all_instance/(1024*1024*1024)
    print("Sum of all the instances in GB="+str(sum_all_instance_in_gb))

def main():
    if __name__ == '__main__':
        output_arr = readfile("/Users/deepak.sahu/Downloads/list.txt")
        cumm_size(output_arr)
main()
