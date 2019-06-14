#balance = 320000
#annualInterestRate = 0.2
#expected: 29157.09
#balance = 999999
#annualInterestRate = 0.18
#expected: 90325.02

#debug = True
debug = False
NUM_MONTHS=12

#See: https://en.wikipedia.org/wiki/Bisection_method
def bisect(f, a, b, tol, nmax):
    n=1
    while n<nmax:
        c = (a+b)/2 #new midpoint
        if f(c) == 0 or (b-a)/2 < tol:
            return c
        n = n+1
        #cmp(f(x),0) stands in for sign(f(x))
        if cmp(f(c),0) == cmp(f(a),0):
            a = c
        else:
            b = c

def calc_total(payment):
    printd("Calculating total balance for payment: " + str(payment))
    return calc_balance(balance, payment, NUM_MONTHS)

def calc_balance(orig_balance, payment, num_payments):
    #Answer expects interest calc'd after deducting payment (not explicitly stated)
    #interest = orig_balance * monthlyInterestRate
    #new_balance = orig_balance + interest - payment
    interest = (orig_balance - payment) * monthlyInterestRate
    new_balance = orig_balance + interest - payment
    printd("payment: {}\ninterest: {:.2f}\nbalance: {:.2f}".format(NUM_MONTHS-num_payments, interest, new_balance))
    if num_payments > 1:
        return calc_balance(new_balance, payment, num_payments-1)
    else:
        return new_balance

def printd(s):
    if(debug):
        print(s)

def solve():
    global monthlyInterestRate 
    monthlyInterestRate = annualInterestRate / NUM_MONTHS
    lower = balance / NUM_MONTHS
    upper = (balance * (1+monthlyInterestRate)**NUM_MONTHS)/NUM_MONTHS
    printd("lower: " + str(lower))
    printd("upper: " + str(upper))
    printd("f(upper): " + str(calc_total(upper)))
    printd("f(lower): " + str(calc_total(lower)))

    opt_payment = bisect(calc_total, lower, upper, .002, 100000)
    print("{:.2f}".format(opt_payment))
    return round(opt_payment,2)

#uncomment when submitting to EdX
#solve()
