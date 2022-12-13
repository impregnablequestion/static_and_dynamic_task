### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:                            #should be == as we are testing for equality here                           
      return True         
    else                                          # no colon after the else statement
      return False
   

  dif highest_card(self, card1 card2):            # typo, should be spelt 'def', should be a comma after card1
  if card1.value > card2.value:                   # indentation is off on this if statement
    return card                                    # should be return card1
  else:
    return card2
  


def cards_total(self, cards):                     # should be indented or it won't be a method belonging to the function
  total                                           # no definition of the variable, should be set as 'total = 0'
  for card in cards:
    total += card.value
    return "You have a total of" + total          # this statement should be returned outside of the for loop, once all of the cards
                                                  # have been counted, otherwise the function will return after only the first card has been counted.

                                                  # also it should be "You have a total of " with a space at the end so the number doesn't come directly afterwards
```
