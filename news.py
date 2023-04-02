# This is the actual news class, that will store the retrieved information


class News:
  def __init__(self, title, content, date, image, sourceLink) -> None:
    self.title = title
    self.content = content
    self.date = date
    self.image = image
    self.sourceLink = sourceLink
    
  def __str__(self) -> str:
    return self.title + " | " + self.content + " | " + self.date + "| src = " + self.image + " \n"

