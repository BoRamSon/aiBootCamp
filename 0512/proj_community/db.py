class DataBase:
  def __init__(self):
    self.database_member = []
    self.database_posts = []

  def db_member(
        self, 
        member_number, 
        userid, 
        userpawssword, 
        name, 
        phone, 
        email
      ):
    self.database_member.append({
      'member_number': member_number[0],
      'id':userid, 
      'pw':userpawssword, 
      'name':name, 
      'phone':phone, 
      'email':email
    })
    
  def db_posts(
        self, 
        member_number, 
        created_date, 
        created_time, 
        title, 
        content
      ):
    self.database_posts.append({
      'member_number': member_number,
      'created_date':created_date, 
      'created_time':created_time,
      'modify_date':'',
      'modify_time':'',
      'title':title, 
      'content':content
    })