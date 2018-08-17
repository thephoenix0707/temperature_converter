user_choice = int(raw_input("What would you like to do today? \nPress:\n1 for F to C\n2 for C to F\n"));

def f_to_c(temp_f):
    ans_c = (temp_f - 32) * .5556;
    print "%.3f degree Fahrenheit is equivalent to %.3f degree Celcius." %(temp_f, ans_c);

def c_to_f(temp_c):
    ans_f = (temp_c * 1.8) + 32;
    print "%.3f degree Celcius is equivalent to %.3f degree Fahrenheit." %(temp_c, ans_f);

operation = ['F to C', 'C to F'];
if user_choice == 1:
    operation = 'F to C';
    print "You selected to perform F to C.";
    temp_f = float(raw_input("Enter the temperature in degree F: "));
    f_to_c(temp_f);
elif user_choice == 2:
    operation = 'C to F';
    print "You selected to perform C to F.";
    temp_c = float(raw_input("Enter the temperature in degree C: "));
    c_to_f(temp_c);
else:
    print "Invalid selection."


