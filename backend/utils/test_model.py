from prediction import predict_ticket

text = "My system is not working and it is urgent"

category, priority = predict_ticket(text)

print("Category:", category)
print("Priority:", priority)
