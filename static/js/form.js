function validacion()
    {
        fname = document.getElementById("fname").value;
        Apellido = document.getElementById("Apellido").value;
        Empresa = document.getElementById("Empresa").value;
        Cargo = document.getElementById("Cargo").value;
        Email = document.getElementById("Email").value;

        if (fname === '') 
        {
        document.getElementById('error').innerHTML = "Tenes que completar todos los datos!";
            return false;
        }
        else if (Apellido === '') {
            document.getElementById('error').innerHTML = "Tenes que completar todos los datos!";
            return false;
        }
        else if (Empresa === '') {
            document.getElementById('error').innerHTML = "Tenes que completar todos los datos!";
            return false;
        }
        else if (Cargo === '') {
            document.getElementById('error').innerHTML = "Tenes que completar todos los datos!";
            return false;
        }    
        else if (Email === '') {
            document.getElementById('error').innerHTML = "Tenes que completar todos los datos!";
            return false;
        }  
        return true;
    }