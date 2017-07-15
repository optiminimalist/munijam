import time

from nextbus import get_raw_muni_data

if __name__ == "__main__":
    while(True):
        try:
            response = get_raw_muni_data()
            fname = "tmpdata/"+ str(int(time.time())) + ".xml"
            with open(fname, 'w') as f:
                f.write(response)
                print("Wrote: "+fname)
        except:
            print("Error")
        print("Sleeping....")
        time.sleep(300)
