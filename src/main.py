# main.py

from code_review.analyzer import CodeAnalyzer
from code_review.git_integration import GitIntegration
from code_review.suggestions import CodeSuggestions

def main(repo_path):
    # Initialize GitIntegration with the repository path
    git_integration = GitIntegration(repo_path)

    # Fetch code from Git repository
    code = git_integration.fetch_code()

    # Initialize CodeAnalyzer with the fetched code
    code_analyzer = CodeAnalyzer(code)

    # Perform code analysis
    errors, inefficiencies, best_practices = code_analyzer.analyze()

    # Generate suggestions based on analysis results
    suggestions = CodeSuggestions(errors, inefficiencies, best_practices).generate_suggestions()

    # Commit suggestions back to Git repository
    git_integration.commit_suggestions(suggestions)

if __name__ == "__main__":
    # Replace 'repo_path' with the actual path to your Git repository
    repo_path = '/path/to/your/git/repository'
    main(repo_path)
