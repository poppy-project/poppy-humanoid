#Various Poppy scene for V-REP

poppy_humanoid.ttt : 	The scene directly import with the URDF file made by Solidworks. The closest scene to the reality.
						This scene is not recommended to be used with the physic engine Bullet because the very light inertia 
						doesn't work good with Bullet - For some motors, the goal position can be really far from the real position.
						This scene can be used with the physic engine Vortex.
						

Poppy_humanoid_inertia : 	In this scene, the inertia is multiplied by 4 for all shapes. So, the simulation with the physic engine
							Bullet works really better. The speed and the position for motors is not so far from the goal. The PID of
							all motors is also modified with I = 0,01.
						

						
Poppy_humanoid_add_force : 	The same scene that Poppy-humanoid_inertia but a force (add with a lua child script) push Poppy in a random direction. Could be useful
							to test balance behaviour for poppy.