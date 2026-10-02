from app.main import main

def test_main_application_name(capsys):
    main() #application main function

    # Retrieve the standard output and standard error captured by pytest
    captured_output = capsys.readouterr() 

    assert captured_output.out == "Space Weather Operations Dashboard\n"