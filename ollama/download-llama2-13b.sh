#!/bin/bash
 
process1() {
  ollama serve &
  sleep 10
}
 
process2() {
  ollama pull llama2:13b
}
 
process1 
process2

pkill ollama
wait
 
echo "All processes have completed."
