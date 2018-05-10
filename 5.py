def Exercise5():
        s=''
        for i in ('+','-',''):
            for j in ('+', '-', ''):
                for k in ('+', '-', ''):
                    for l in ('+', '-', ''):
                        for m in ('+', '-', ''):
                            for n in ('+', '-', ''):
                                for o in ('+', '-', ''):
                                    for p in ('+', '-', ''):
                                        s='1'+i+'2'+j+'3'+k+'4'+l+'5'+m+'6'+n+'7'+o+'8'+p+'9'
                                        if eval(s)==100:
                                            print(s,end='=100\n')

Exercise5()
