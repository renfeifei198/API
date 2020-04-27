'''
生成caseID
'''

class generate():

    def generateCaseID(self ,case_name):
        caseID = []
        for a in range(1 ,10001):
            a = caseID.append(case_name +str(a))
        return caseID


if __name__ == '__main__':

    print(generate().generateCaseID('login_'))