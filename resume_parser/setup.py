import subprocess
import sys
import os

def install_requirements():
    print("\nInstalling Python packages from requirements.txt...\n")
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install',
        '--default-timeout=300',
        '-r', 'requirements.txt',
        '--trusted-host', 'pypi.org',
        '--trusted-host', 'files.pythonhosted.org'
    ])

def download_spacy_model():
    print("\nDownloading spaCy language model (en_core_web_sm)...\n")
    subprocess.check_call([
        sys.executable, '-m', 'spacy', 'download', 'en_core_web_sm'
    ])

def run_tests():
    print("\nRunning tests to verify installation...\n")
    subprocess.check_call([
        sys.executable, '-m', 'pytest'
    ])

def main():
    print("Starting Resume Parser Setup")
    
    install_requirements()
    download_spacy_model()
    run_tests()

    print("\nSetup complete. You're ready to run the parser!\n")
    print("Example: python -m parser.cli -i demo_resumes/sample_resume.pdf -o output.json -v")

if __name__ == "__main__":
    main()
