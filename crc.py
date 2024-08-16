sendData = "100100"
key = "1101"

def senderData(data):
    
    keyLen = len(key) - 1
    dataWord = data + "0" * keyLen

    decimalData = int(dataWord, 2)
    decimalKey = int(key, 2)
    result = decimalData % decimalKey

    remainder = bin(result)[2:]

    new_dataWord = data + remainder 

    print("Sender:")
    print("Data: ", data)
    print("Key: ", key)
    print("CRC data: ", dataWord)
    print("Sender data word: ", new_dataWord)
    return new_dataWord, result

def receiverData(sendData, ogiAns):
    data = sendData[:-len(key) + 1] 
    remainder = sendData[len(data):]  

    decimalData = int(data + remainder, 2)
    decimalKey = int(key, 2)
    result = decimalData % decimalKey

    print("\nReceiver:")
    
    if result == "0":
        print("There is no error in your code!")
    else:
        print("There is some error in your code!")
    
    
    print("The remainder is: ", result)
    print("The original remainder was: ", ogiAns)
        
if __name__ == "__main__":
    dataWord, remainder = senderData(sendData)
    receiverData(dataWord, remainder)