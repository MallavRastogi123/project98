def swapping_file_data():
    data_a=open("sample1.txt","r");
    data_a=data_a.read();
    data_b=open("sample2.txt","r");
    data_b=data_b.read();
    with open("sample1.txt","w") as a:
        a.write(data_b);
    with open("sample2.txt","w") as a:
        a.write(data_a);

swapping_file_data();