student = {
    "name": "amir ch",
    "subjects": {
        "phycics": 97,
        "chemistry" : 98,
        "mathematics" : 96,
        "english" : 99 
        }
}

### keys 
#print (len(list(student.keys())))

### values dictionary
#print (student.values()) # if we wang change into list print (list(student.keys())

### itemes dictionary ( return all key value as tuple )
#print (student.items())
 
### .get return the key according to value # both are same output but different is that .get 
# always output none and other is error output 
#print (student ["name2"]) # error
#print (student.get("name2")) # none output

### update method
student.update({"city" : "lahore"})
print (student)