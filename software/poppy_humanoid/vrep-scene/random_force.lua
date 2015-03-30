-- Put this lua script as child threated script and poppy will be push every 2 seconds with a random force in a random direction

if (sim_call_type==sim_childscriptcall_initialization) then

	
	handle=simGetObjectHandle('chest_respondable')
	t0 = simGetSimulationTime()
	
	

end


if (sim_call_type==sim_childscriptcall_actuation) then
	
	
	if  simGetSimulationTime()-t0>2 then  
		t0 = simGetSimulationTime()
		fx = math.random(3,8)
		fy = math.random(3,8)
		fz = math.random(3,8)	
		simAddForce(handle,{0,0,0},{fx,fy,fz})
		
	end

	

end


if (sim_call_type==sim_childscriptcall_sensing) then

	-- Put your main SENSING code here

end


if (sim_call_type==sim_childscriptcall_cleanup) then

	-- Put some restoration code here

end