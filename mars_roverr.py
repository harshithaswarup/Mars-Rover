class Nasa(object):
    def give_commands(self,get_direction):
        rover_direction = get_direction
        return rover_direction

    def get_moves(self,rover_direction):
        move_rover = rover_direction.split(' ')
        return move_rover

    
class Plateau:
    def __init__(self,length,breadth,rover_list):
        self.length = length
        self.breadth = breadth
        self.rover_list = rover_list

    def create_rover(self,get_id):
        new_rover = get_id
        return new_rover

    def add_rover(self,new_rover):
        self.rover_list.append(new_rover)
        return self.rover_list



class Rover(Plateau):
    def __init__(self,length,breadth,rover_list,x_axis,y_axis,rover_heading,ID):
        Plateau.__init__(self,length,breadth,rover_list)
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.rover_heading = rover_heading
        self.ID = ID


    def move_left(self,rover_direction):
        n = Nasa()
        n.give_commands(rover_direction)
        move_rover = n.get_moves(rover_direction)
        if(self.rover_heading == 'N'):
            self.y_axis += 1
            return self.y_axis

        elif(self.rover_heading == 'S'):
            self.y_axis -= 1
            return self.y_axis

        elif(self.rover_heading == 'E'):
            self.x_axis += 1
            return self.x_axis

        else:
            self.x_axis -= 1
            return self.x_axis

    def move_right(self,rover_direction):
        if(self.rover_heading == 'N'):
            self.y_axis += 1

        elif(self.rover_heading == 'S'):
            self.y_axis -= 1

        elif(self.rover_heading == 'E'):
            self.x_axis += 1

        else:
            self.x_axis -= 1

class Directions(Rover):
    def __init__(self,length,breadth,rover_list,x_axis,y_axis,rover_heading,ID,directions=[]):
        Rover.__init__(self,length,breadth,rover_list,x_axis,y_axis,rover_heading,ID)
        self.directions=directions

    def turn_left(self,rover_direction):
        n = Nasa()
        n.give_commands(rover_direction)
        n.get_moves(rover_direction)
        
        if(self.rover_heading == 'N'):
            self.rover_heading = 'W'
            return self.rover_heading

        elif(self.rover_heading == 'S'):
            self.rover_heading = 'E'
            return self.rover_heading

        elif(self.rover_heading == 'E'):
            self.rover_heading = 'N'
            return self.rover_heading
              
        else:
            self.rover_heading = 'S'
            return self.rover_heading


    def turn_right(self,rover_direction):
        if(self.rover_heading == 'N'):
            self.rover_heading = 'E'
            return self.rover_heading

        elif(self.rover_heading == 'S'):
            self.rover_heading = 'W'
            return self.rover_heading


        elif(self.rover_heading == 'E'):
            self.rover_heading = 'S'
            return self.rover_heading
              
        else:
            self.rover_heading = 'N'
            return self.rover_heading
            
      
            
if __name__=='__main__':

    process = True
               
    d = Directions(5,5,['x1'],0,0,'E','x1',['N','S','E','W'])

    while process:
        print('Enter L to turn the rover left')
        print('Enter R to turn the rover right')
        print('Enter M to move the  left')

        print "The initial position of the rover is:",'(',d.x_axis,d.y_axis,d.rover_heading,')'
        rover_direction=raw_input("Give the range of input for the rover")
        n = Nasa()
        n.give_commands(rover_direction)
        move_rover = n.get_moves(rover_direction)
        rover_direction = n.give_commands(rover_direction)
        for movement in move_rover:
            if(movement == 'L'):
                n = Nasa()
                n.give_commands(rover_direction)
                move_rover = n.get_moves(rover_direction)
                d.turn_left(rover_direction)
                if(movement == 'M'):
                    d.move_left(rover_direction)
            else:
                d.turn_right(rover_direction)
                if(movement == 'M'):
                    d.move_right(rover_direction)
                    

        print "The current position of the rover is:",'(',d.x_axis,d.y_axis,d.rover_heading,')'

        if((d.x_axis == d.length) or (d.x_axis == -d.length) or (d.y_axis == d.breadth) or (d.y_axis == -d.breadth)):
            print "Boundary !!!!"
            user_choice = raw_input("would u like to create another rover?")
            choice = ['yes','no']
            if(user_choice == 'yes'):
                new_rover = raw_input("Enter the new ID of the rover:")
                new_rover = d.create_rover(new_rover)
                rover_list = d.add_rover(new_rover)
            else:
                process = False


