import pandas as pd
import sys
import random
from timeit import default_timer as timer

def power(a,b,m):
    """
    Calculate 'a' power 'b' modulo 'm' using binary exponentiation
    """
    a = a%m
    res = 1
    while b>0:
        if b&1:
            res = res * a % m
        a = a * a%m
        b = b>>1
    return res

def isprime(n):
    """
    Check if a given number 'n' is prime or not

    """
    maximum_limit = int(n**(0.5))

    # Checking if N is divisible by 2 as all even numbers except 2 are non-prime 
    if n<2 or (n%2==0 and n>2):
        return False
    
    # Cheking if the number N is divisible by i until sqrt(N)
    for i in range(3,maximum_limit+1,2):
        if(n%i==0):
            return False
    return True

def generate_primes(a,b):

    """
    Generate all primes in the range (a,b) inclusive

    """

    primes = [] #List to store the generated prime numbers
    for i in range(a,b+1):
        if isprime(i):
            primes.append(i)
    
    # As we need 3 primes P,Q,R for the Modified RSA Algorithm
    if len(primes)<3:
        raise ValueError('The range of a and b is very small')
    
    return primes

def inverse(e, phi_n):

    """
    Calculating the multiplicative inverse of (e,phi_n) using 
    Euclid's extended algorithm

    """
    a = phi_n
    b, c = 0, 1

    if phi_n==1:
        return 0
    
    while e>1:
        q = e//phi_n
        x = phi_n
        phi_n = e%phi_n
        e = x
        x = b
        b = c - q * b
        c = x
    if c<0:
        c = c+a
    return c
        
def gcd(a,b):
    """
    Calculate the GCD of two numbers (a,b) using Euclidean algorithm

    """
    if a==0:
        return b
    return gcd(b%a,a)

def generate_keys(p,q,r):

    n = p*q*r
    
    phi_n = (p-1)*(q-1)*(r-1) #totient

    # 'e' is any integer between 1 and phi_n which is coprime with phi_n
    e = random.randint(2,phi_n-1)

    # Checking if the generate random 'e' is coprime with phi_n
    while gcd(e,phi_n)!=1:
        e = random.randint(2,phi_n-1)

    # 'd' is used for private key
    d = inverse(e,phi_n)

    #Public Key: (e,n) and Private Key: (d,n)
    return [(e,n), (d,n), phi_n]

def encrypt_message(message, df1, df2):
    
    # Reading the data store in csv files to respective dataframes
    #df1 = pd.read_csv('table1.csv')
    #df2 = pd.read_csv('table2.csv')
    
    # Getting 'e' and 'n' out of the dataframes to make public key
    e = int(df2[0][1])
    n = int(df1[0][3])

    # 'encrypted_txt' is a list containg respective encrypted characters for each and every char in the input text
    encrypted_txt = []
    for char in message:
        elem = power(ord(char),e,n) # ord(char) is used to convert the characters to respective integer format (Using binary exponentiation)
        #elem = ord(char)**e
        encrypted_txt.append(elem)

    return encrypted_txt # Returning the list of encrypted characters
    
def decrypt(message, df1, df2):
    # Reading the data store in csv files to respective dataframes
    #df1 = pd.read_csv('table1.csv')
    #df2 = pd.read_csv('table2.csv')
    
    # Getting 'd' and 'n' out of the dataframes to make private key
    d = int(df2[0][2])
    n = int(df1[0][3])
    
    # 'decrypted_msg_list' is a list containg respective decrypted characters for each and every char in the encrypted list
    decrypted_msg_list = []
    
    for char in message:
        #decrypted_msg_list.append(chr((char**d)%n))
        decrypted_msg_list.append(chr(power(char,d,n))) # Using Binary exponentiation 
    
    # Joining all the characters in the 'decrypted_msg_list' to get the final decrypted message as string
    decrypted_txt = ''.join(decrypted_msg_list)
    
    return decrypted_txt

if __name__ == '__main__':
    startTime = timer()

    # Generate all the prime numbers between two numbers
    primes = generate_primes(100,200)
    
    # Generate random numbers between 0 and len(primes)-1 to get the index to select a prime number from the list
    p = random.randint(0,len(primes)-1)
    q = random.randint(0,len(primes)-1)
    r = random.randint(0,len(primes)-1)

    # Generate the random numbers until we get P,Q,R to be unique indices
    while p==q or p==r or q==r:
        p = random.randint(0,len(primes)-1)
        q = random.randint(0,len(primes)-1)
        r = random.randint(0,len(primes)-1)
    
    # Assigning respective prime number from the 'primes' list
    p = primes[p]
    q = primes[q]
    r = primes[r]

    # Generate public key, private key and phi_n using the prime numebers P,Q,R
    public_key,private_key,phi_n = generate_keys(p,q,r)
    print(f'P: {p}, Q: {q} and R: {r}')
    print(f'Public Key: {public_key} and Private Key: {private_key} and phi_n: {phi_n}')
    
    # Get e,d,n from public key and private key
    e,d,n = public_key[0],private_key[0],public_key[1]
    
    # Converting to dataframes respective for offline storage of required variable
    df1 = pd.DataFrame([p,q,phi_n,n])
    df2 = pd.DataFrame([r,e,d])
    
    # Storing p,q,phi_n,n into 'table.csv'
    #df1.to_csv('table1.csv')
    #Storing r,e,d into 'table2.csv'
    #df2.to_csv('table2.csv')

    # Taking the message to encrypted as input
    if len(sys.argv)!=2:
        print(f'USAGE: {__file__} <input file>')
        sys.exit(1)
    input_filename = sys.argv[1] # Text file name as input in the second argument
    
    # Reading the input text file into a variable 'message'
    with open(input_filename, 'r') as file:
        message = file.read()
    
    #print('.....ENCRYPTING YOUR TEXT.....')
    encrypted_msg_list = encrypt_message(message, df1, df2) # Encrypting the input message
    #encrypted_txt = ""
    # Converting the encrypted message list into a string to be stored
    #for item in encrypted_msg_list:
    #    encrypted_txt+=(str(item))
    #print('.....ENCRYPTION SUCCESSFUL.....')
    
    # Writing the encrypted message into a seperate text file
    #with open('encrypted.txt','w') as file:
    #    file.write(encrypted_txt)
    #print(".....ENCRYPTED MESSAGE WRITTEN IN 'encrypted.txt'..... ")
   
    #print('.....DECRYPTING THE ENCRYPTED TEXT.....')
    decrypted_txt = decrypt(encrypted_msg_list, df1, df2) #Decrypting the encrypted message for verification
    print(decrypted_txt)
    # Writing the decrypted message into another text file
    #with open('decrypted.txt','w') as file:
    #    file.write(decrypted_txt)
    #print('.....DECRYPTION SUCCESSFUL.....')
    #print(".....DECRYPTED MESSAGE WRITTEN IN 'decrypted.txt'..... ")

    endTime = timer()

    print((endTime - startTime) * 1000.0, ' s') 