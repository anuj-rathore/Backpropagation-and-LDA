import numpy as np
import math

numberPatterns = [0,1,3]
def sigmoid(z):
    val = 1/(1 + np.exp(-z))
    return val

def sigmoiddiff(z):
    val = sigmoid(z)
    return val*(1-val)

def truevalue(z):
    if z == 0:
        return [0, 0]
    elif z == 1:
        return [0, 1]
    elif z == 3:
        return [1, 1]

def preprocess(filename):
    processedData = []
    numbers = []
    count = [0]*8
    with open(filename) as trainingdata:
        content = trainingdata.read().splitlines()
        content = content[21:]
        tempImage = [1]

        for i in range(len(content)):
            if (i % 33) % 4 == 0 and i % 33 != 0:
                for k in range(len(count)): #len(count)=8
                    if count[k] >=8:
                        tempImage.append(1)
                    else:
                        tempImage.append(0)
                # print i, len(tempImage)
                count = [0]*8
                
                
            if (i - 32) % 33 == 0:
                value = int(content[i])
                if value in numberPatterns:
                    
                    numbers.append(value)
                    processedData.append(tempImage)
                tempImage = [1]
                continue
            for j in range(len(content[i])):
                count[j/4] += int(content[i][j])    
    

    # for i in range(len(numbers)):
    #     print numbers[i],
    #     print processedData[i]
    
    return numbers, processedData
    
    # print numbers


hidden_layer = 15;
no_of_epochs = 1;

if __name__ == '__main__':
    numbers, processedData = preprocess('optdigits-orig.tra')
    
    train_labels = []
    test_labels = []

    train_data = []
    test_data = []
    
    eta = 0.5
    wkj = 2*np.random.random((hidden_layer,2))-1
    wji = 2*np.random.random((65,hidden_layer))-1
    z = [0,0]

    J = 0;    
    for i in range(len(numbers)):
        if i<500:
            # print numbers[i]
            train_labels.append(numbers[i])
            train_data.append(processedData[i])

        else:
            test_labels.append(numbers[i]) 
            test_data.append(processedData[i])

    # x = train_data[:]
    # print(len(train_data))
    
    for epochs in range(no_of_epochs):
        for img in range(len(train_data)):
            n = train_labels[img]
            x = np.array(train_data[img])
            # print x
            # break
            netj = np.dot(x,wji)
            # print netj
            # break
            temp = 1 + np.exp(-netj)
            y = 1/temp
            netk = np.dot(y,wkj)
            temp = 1 + np.exp(-netk)
            z = 1/temp

            diff = truevalue(n) - z
            backup = wkj

  #           #Backpropagation Starts

            deltak = []

            for k in range(2):
                sigmoid = 1 / (1 + np.exp(-netk[k]))
                sigmoiddif = sigmoid*(1-sigmoid)
                dell = diff[k]*sigmoiddif
                deltak.append(dell)
                for j in range(hidden_layer):
                    delta = eta * dell * y[j]
                    wkj[j][k] = wkj[j][k] + delta

  #           #%updating weights input to hidden
            for j in range(hidden_layer):
                sigmoidj = 1 / (1 + np.exp(-netj[j]))
                sigmoiddifj = sigmoidj*(1-sigmoidj)
                term = 0
                for k in range(2):
                    term = term + backup[j][k]*deltak[k]
                tmp = term * sigmoiddifj
                #tmp has 2 elements each
                for i in range(65):
                    delta = eta*tmp*x[i]
                    # print delta
                    wji[i][j] = wji[i][j] + delta
            # print wkj
            # print diff
            # break
        # print wji
    # break

    #TEST DATA
    result = 0
    for img in range(len(test_data)):
        n = test_labels[img]
        x = np.array(test_data[img])
        netj = np.dot(x,wji)
        temp = 1 + np.exp(-netj)
        y = 1/temp
        netk = np.dot(y,wkj)
        temp = 1 + np.exp(-netk)
        z = 1/temp

        for i in range(2):
            if (z[i]>0.5):
                z[i] = 1
            else:
                z[i] = 0
        
        if (truevalue(n)[0] == z[0] and truevalue(n)[1] == z[1]):
            result = result + 1    

    print "Number of epochs:"
    print no_of_epochs
    print "Number of hidden layers:",
    print hidden_layer

    print "RESULT"
    print result
    accuracy = (result/86.0)*100.0;

    print "ACCURACY"
    print accuracy,
    print "%"

    print "Input to hidden weights"
    print wji

    print "hidden to ouput weights"
    print wkj

