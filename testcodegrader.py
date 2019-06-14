import edxcodegrader

results = []

def test(balance, rate, expected):
    passed = False
    print("Balance: {:.2f}\nRate: {:.2f}".format(balance, rate))
    #print("{:.2f}".format(opt_payment))
    edxcodegrader.balance = balance
    edxcodegrader.annualInterestRate = rate 
    actual = edxcodegrader.solve()
    if(actual >= expected-.02 and actual <= expected+.02):
        passed = True
    print("Expected: {:.2f}".format(expected))
    print("Actual: {:.2f}".format(actual))
    #print("PASSED") if(passed) else print("FAILED")
    print("PASSED" if passed else "FAILED")
    print
    return passed

results.append( test(320000, 0.2, 29157.09) )
results.append( test(999999, 0.18, 90325.02) )
results.append( test(265834, 0.22, 24432.64) )
results.append( test(18381, 0.2, 1674.80) )
results.append( test(127131, 0.18, 11483.12) )
results.append( test(370937, 0.18, 33504.93) )
results.append( test(127963, 0.18, 11558.27) )
results.append( test(283549, 0.22, 26060.81) )
results.append( test(246326, 0.22, 22639.67) )
results.append( test(63906, 0.21, 5848.19) )
results.append( test(106796, 0.21, 9773.15) )
results.append( test(314301, 0.2, 28637.82) )

numPassed = len(list(filter(lambda x: x, results)))
numFailed = len(results) - numPassed
print("Passed: {:d}\tFailed: {:d}\tTotal: {:d}".format(numPassed, numFailed, len(results)))

