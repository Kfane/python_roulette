# python_roulette
A python program that makes a Firearm class and uses it.

Welcome To Python Roulette!

Feeling lucky? Test it out!

To run code, run program as is for the basic shell example.

The classes involed in this program are Firearm and Users. Users
is just simply a list of strings containing names and the class also stores
how many users there are in the Users list. 

Along with Users, there is a more interesting class named Firearm. It
emmulates a revolver that can hold 6 rounds. The constructor simply requires
you to pass how many bullets should be loaded in the gun. Then use the fill_gun 
method to load the amount of the bullets passed in. Add_ammo allows you to pass
more ammo into the the gun.(Still haing to use fill_gun) Get_ammo returns the ammount
of ammo currently loaded in the gun. Expell_one_bullet changes the number of bullets loaded
in the gun by one. Get_bullet_list returns a list (default chamber size is set to 6 bullets
at max) with boolean values cordinating with weather that position in the chamber contains 
a bullet. True meaning that there is a bullet there. Shoot will choose a random position (as 
if spinning the chamber) within the bullet list. The value if the bullet is in that position
is returned. Then that position is set to false, if it was true it is as if the bullet has left 
that position.

The main function handles game rules and inputs.
