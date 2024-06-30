from scripts.scriptgen import generate_script

def main():
    prompt = "Create a script about the top 5 parks in Los Angeles."
    script = generate_script(prompt)
    if script:
        print("Generated Script:")
        print(script)
    else:
        print("Script generation failed.")

if __name__ == "__main__":
    main()
