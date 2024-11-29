'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile
# zipfile is a utility that allows you to work with zip files

# The following method had this thought process:
# zf_handle is the zip and password is... obviously the password but in byte format
# now, we try to extract the zip using a password. If cracked, we return True
# along with password, so we know it.
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password) # Attempt to extract zip using pass
        print(f"[+] Cracked! Using {password.decode()}") # Print if succeeded
        return True 
    except RuntimeError:
        return False
    except Exception as e:
        print("[-] An error occured:", e)
        return False

def main():
    print("[+] Beginning bruteforce... ")
    with ZipFile('enc.zip') as zf: # Using enc.zip as zf
        with open('rockyou.txt', 'rb') as f: # Opening rockyou.txt as f
            # Iterate through password entries in rockyou.txt
            for password in f:
                password = password.strip() # Get those newlines off

                if attempt_extract(zf, password): # If password has been cracked
                    return
    print("[-] Password not found in list")

if __name__ == "__main__":
    main()
