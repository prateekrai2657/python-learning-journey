# Magic mthods = Dunder methods (double underscore) __init__,__str__,__eq__ and manymore 
#                 They are automatically called by many Phython's built in-operations.
#                 They allow developers to define or customize the behaviour of subjects 

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title     
        self.author = author     
        self.num_pages = num_pages
         
    def __str__(self):
        return f"'{self.title}' by {self.author} containing {self.num_pages}"  
    
    def __eq__(self,other):
        return self.title==other.title and self.author == other.author
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
            return f"{self.num_pages+ other.num_pages} pages"
        
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == "title":
            return self.title 
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else :
            print("************")
            return f"key '{key}' was not found!!"
            

book1 = Book("The Hobbit" , "J.R.R Tolkien" , 310)   
book2 = Book("Harry Potter and The Philospher's Stone " , "J.K Rowling" , 223)   
book3 = Book("The Lion, The Witch and the Wardrobe" , "C.S Lewis" , 172) 
book4 = Book("The Hobbit" , "J.R.R Tolkien" , 310)  

# print(book2)
# print(book3)
# print(book1==book4)
# print(book3 < book4)
# print(book4>book2)
# print(book2+book4)
# print("Harry" in book2)
print(book1['author'])
print(book2['title'])
print(book3['num_pages'])
print(book3['audio'])