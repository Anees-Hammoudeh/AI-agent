from functions.write_file import write_file

# اختبار 1: كتابة ملف عادي
result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(result)

# اختبار 2: كتابة ملف داخل مجلد فرعي
result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result)

# اختبار 3: محاولة الكتابة خارج working_directory
result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(result)
