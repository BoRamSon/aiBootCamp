class DataBase:

  def db_member(
        self, 
        member_number, 
        userid, 
        userpawssword, 
        name, 
        phone, 
        email
      ):
    database_member = {
      'member_number': member_number,
      'id':userid, 
      'pw':userpawssword, 
      'name':name, 
      'phone':phone, 
      'email':email
    }
    return database_member
    
  def db_posts(
        self, 
        writing_number,
        member_number, 
        created_date, 
        created_time, 
        title, 
        content,
        hits = 0
      ):
    database_posts = {
      'writing_number': writing_number,
      'member_number': member_number,
      'created_date':created_date, 
      'created_time':created_time,
      'modify_date':'',
      'modify_time':'',
      'title':title, 
      'content':content,
      'hits' : hits
    }
    return database_posts