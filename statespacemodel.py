import numpy as np


# Define A matrix
# Here A matrix is identity matrix
# A is sometimes equivalent to saying F  , So A and F are identical

# global state_est_t_minus_1 ( ek extra line likhi thi apn ne toh woh error aa rha tha )

A_t_minus_1 = np.array([[1 , 0 , 0] ,
                        [0 , 1 , 0 ],
                        [0  , 0 , 1 ]])


# A_t_minus_1 = np.identity(3)

# The estimated state vector at time t-1 in global refrence frame

state_est_t_minus_1 = np.array([0,0,0])

# The control input vector at time t-1 in global refrence frame [ linear velocity , yaw rate ]

control_vec_t_minus_1 = np.array([4.5 , 0.05])

# Noise applied in the forward motion model
# The size of the noise vector is actually equal to VECTOR ( column vec ) with size equal to no. of states

process_noise_t_minus_1  = np.array([0.02 , 0.01 , 0.004])   # Question is how to decide this

# Initialization is any ALGO , check how to or how to decide on the values to be taken to intialize the algorithm

yaw_angle = 0  # IN radians

deltat = 1  # sec

# Calculates and returns the matrix B , the jacobian that is required B matrix is STATES cross control inputs
# A matrix is STATES cross STATES
# def function name ( argument )

# while defining the function use colon ( remember that ) #two parameters as output , yaw and dt

def getB(yaw,dt) :
    B = np.array( [[  np.cos(yaw)*dt , 0],
               [np.sin(yaw)*dt ,0 ],
              [0,dt] ] )
    return B
# return B  # so we want the result of B to be used as or for further calculation

# This is after first iteration 
def main() :
    state_est_t = A_t_minus_1 @ state_est_t_minus_1 + (getB(yaw_angle, deltat)) @ (control_vec_t_minus_1) + (process_noise_t_minus_1)
    # print(f'State at time t-1 : {state_est_t_minus_1}')
    print(f'State at time t-1 : {state_est_t_minus_1}')
    print(f'Control input value at t-1 : {control_vec_t_minus_1}' )
    print(f'State at time t: {state_est_t}' )
    # state_est_t_minus_1 = state_est_t   Cannot modify it from inside the function 




main() 

# # This shoud be outside of the indentation to be executed 

# # input two matrices
# mat1 = np.array([[1, 6, 5],[3 ,4, 8],[2, 12, 3]])
# mat2 = np.array([[3, 4, 6],[5, 6, 7],[6,56, 7]])

# if __name__ = "__main__" 
#Used for making the IMP. stufff available to you to be used from different file .




# print("hello world")
# print(f'value of mat1 is {mat1}') 
# print(f'value of mat2 is {mat2}') 

# res = np.dot(mat1,mat2)

# print(f'Value of res is : \n {res}')

# resop = mat1 @ mat2 

# print(f'Value of resop is : \n \n {resop} ' )



