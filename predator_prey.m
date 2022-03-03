% Solution of Predator-Prey Equations using the Extended Kalman Filter


% State space model

 delt = 0.01; % Time step interval

 c1 = 300; c2 = 200; % Predator-Prey model parameters
 sigma_x = 1; % State noise standard deviation
 Q_n = sigma_x^2*eye(2); % State noise covariance matrix
 H_n = [1 1]; % Measurement matrix
 sigma_y = 1000; % Measurement noise standard deviation
 R_n = sigma_y^2; % Measurement noise covariance matrix


 
 % Initialization
 x(1:2,1) = [400; 100]; % Initial prey and predator populations


 m(1:2,1) = x(1:2,1); % Gaussian posterior mean at time step 1
 P(1:2,1:2,1) = 100*eye(2); % Gaussian posterior covariance 

 y_collected = []

 % Predator-Prey estimation using extended Kalman filter
 for n = 2 : 2000 , % Time steps

 % State propagation
 v_n = sigma_x*randn(2,1); % State noise vector
 x(1:2,n) = f(x(1:2,n-1)) + v_n; % Markov nonlinear Gaussian evolution

 % Generate measurements
 w_n = sigma_y*randn(1,1); % Measurement noise vector

 % y_n = h(x(1:2,n)) + v_n 


 y_n = H_n*x(1:2,n) + w_n; % Linear Gaussian measurements

 y_collected(end+1) = y_n ; 

 % State-transition function Jacobian matrix
 Ft_n = [1 + delt*(1-m(2,n-1)/c2) -delt*m(1,n-1)/c2;...
 delt*m(2,n-1)/c1 1-delt*(1-m(1,n-1)/c1)];

 % Jacobian of the measurement matirx ( Ht_n ) if in case measurement model
 % is non-lineaer ( Suppose take y_n = x_n^2 ) 
 % har mean pe value nikalni padegi 
 % jaise upar Ft_n ka nikala gaya hai 
 % H = [ 0 2*x_2 ] 



 % Compute Gaussian posterior mean and covariance at time step n
 [m(1:2,n),P(1:2,1:2,n)] = extended_kf (m(1:2,n-1),P(1:2,1:2,n-1),y_n,@f,Ft_n,Q_n,@h,H_n,R_n);
 
 end


 % Plot actual and estimated predator-prey populations
 % Evolution in time
 t = [0:1999]'*delt;
 figure, plot(t,x(1,:),'b'); hold on, plot(t,m(1,:),'r--');
 hold on, plot(t,x(2,:),'g.-'); hold on, plot(t,m(2,:),'m-.');
 xlabel('time'); ylabel('population');
 title('Solution of predator-prey equations using extended Kalman filter');
 legend('actual preys','estimated preys','actual predators',...
 'estimated predators');
 % Phase plot
 figure, plot(x(1,:),x(2,:),'b'); hold on, plot(m(1,:),m(2,:),'r--');
 xlabel('prey population'); ylabel('predator population');
 title('Solution of predator-prey equations using extended Kalman filter');
 legend('actual','estimated');


 %plot of measurements 
 
 figure 
 t = [1:1999]'*delt;
 plot(t,y_collected','b'); 
 title('Measurement of y ');


 
