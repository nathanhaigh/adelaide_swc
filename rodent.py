# tag ID: A8103
# size (oz)
# sightings per month

# is_large (size > 5oz)
# is_small (size < 3oz

class Rodent:
  def __init__(self, tag_id, size):
    # initialise default rodent options
    self.tag_id = tag_id
    self.size = size
    self.sightings_per_month = {}
    
  def is_large(self):
    # return True if size is > 5oz
    #pass
    return(self.size > 5)
  def is_small(self):
    # return True is size < 3oz
    #pass
    return(self.size < 3)
  def plot(self):
    # return the letter of the plot at which this rodent was first captured
    #pass
    return self.tag_id[0]
  def capture(self, month):
    # we captured this rodent once in this month
    #pass
    if month not in self.sightings_per_month:
      self.sightings_per_month[month] = 0
    self.sightings_per_month[month] += 1


