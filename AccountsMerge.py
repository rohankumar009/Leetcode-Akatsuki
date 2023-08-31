class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}  # Maps emails to account names
        graph = {}  # Represents email connections
        
        # Build the graph and email-to-name mapping
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in graph:
                    graph[email] = set()
                if account[1] != email:  # Skip self-connection
                    graph[account[1]].add(email)
                    graph[email].add(account[1])
        
        def dfs(email, group):
            group.add(email)
            for neighbor in graph[email]:
                if neighbor not in group:
                    dfs(neighbor, group)
        
        merged_accounts = []
        visited_emails = set()
        
        # Traverse the graph and merge accounts
        for email in graph:
            if email not in visited_emails:
                group = set()
                dfs(email, group)
                
                merged_account = [email_to_name[email]] + sorted(list(group))
                merged_accounts.append(merged_account)
                visited_emails.update(group)
        
        return merged_accounts
