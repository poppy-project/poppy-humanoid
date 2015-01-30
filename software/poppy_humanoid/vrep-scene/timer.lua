-- DO NOT WRITE CODE OUTSIDE OF THE if-then-end SECTIONS BELOW!!

if (sim_call_type==sim_childscriptcall_initialization) then
  simSetScriptAttribute(sim_handle_self,sim_childscriptattribute_automaticcascadingcalls,false)
end


if (sim_call_type==sim_childscriptcall_actuation) then
  if not firstTimeHere93846738 then
    firstTimeHere93846738=0
  end
  simSetScriptAttribute(sim_handle_self,sim_scriptattribute_executioncount,firstTimeHere93846738)
  firstTimeHere93846738=firstTimeHere93846738+1

------------------------------------------------------------------------------


-- Check the end of the script for some explanations!
  if (simGetScriptExecutionCount()==0) then

  end

  simHandleChildScripts(sim_call_type)

  local currentTime=simGetSimulationTime()

  simSetFloatSignal('CurrentTime',currentTime)

end


if (sim_call_type==sim_childscriptcall_sensing) then
  simHandleChildScripts(sim_call_type)
end


if (sim_call_type==sim_childscriptcall_cleanup) then

  -- Put some restoration code here

end
