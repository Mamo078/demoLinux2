% Implementation of LIE derivative test 
% Make use of syms and jacobian function and declare variables accordingly 




% --------------------input the measurement function------------------%
% --------------------y(x) = h(t,x)-----------------------------------% 



% ----------------f(x) = [ -- , -- , -- , .... ]^T -------------------%
% ---------------- Non-linear function--------------------------------%

% Store the f in cell and the loop around to take the f1 , f2 from it to
% calculate the jacobian 


% ----------------- curly L_f calculation ----------------------------%
% ------------------ max calculate upto (n-1) dim.--------------------%
% Stack all curly L_f's in the Phi matrix 
% jacobian([x*y*(z^3)],[z])

L_f0 = 




% ---------------------Observability matrix---------------------------% 
% Jacobian of Phi w.r.t. states 
% syms x y z
% jacobian([x*y*z,y^2,x + z],[x,y,z]) 
% jacobian( [ f1 , f2 , f3 ] , [ state1 , state2 , state3 ] ) 











