from pans import Basic, Random

class Actions(Random, Basic):
    def goto_time(self):
        print("Click on time tab")
        print("do some logic")
    def goto_my_info(self):
        print("Click on My Info Tab")
        print("do ur logic")

# Single Inh, Multiple, Multilevel