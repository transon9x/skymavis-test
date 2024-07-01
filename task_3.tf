provider "github" {
  token = "###Github_token###"
}

resource "github_team" "team1" {
  name        = "Team1"
  description = "Description of Team1"
}

resource "github_team" "team2" {
  name        = "Team2"
  description = "Description of Team2"
}

resource "github_team" "team3" {
  name        = "Team3"
  description = "Description of Team3"
}

resource "github_team" "team4" {
  name        = "Team4"
  description = "Description of Team4"
}

resource "github_team" "team5" {
  name        = "Team5"
  description = "Description of Team5"
}

resource "github_team" "team6" {
  name        = "Team6"
  description = "Description of Team6"
}

locals {
  memberships = [
    ["User1", "team1", "member"],
    ["User1", "team2", "maintainer"],
    ["User1", "team3", "member"],
    ["User1", "team4", "member"],
    ["User1", "team5", "maintainer"],
    ["User1", "team6", "member"],
    ["User2", "team1", "maintainer"],
    ["User2", "team2", "member"],
    ["User2", "team3", "member"],
    ["User2", "team4", "maintainer"],
    ["User2", "team5", "member"],
    ["User2", "team6", "member"],
    ["User3", "team1", "member"],
    ["User3", "team2", "member"],
    ["User3", "team3", "maintainer"],
    ["User3", "team4", "member"],
    ["User3", "team5", "member"],
    ["User3", "team6", "member"],
    ["User4", "team2", "member"],
    ["User4", "team3", "member"],
    ["User4", "team4", "member"],
    ["User4", "team5", "member"],
    ["User4", "team6", "maintainer"],
    ["User5", "team1", "member"],
    ["User5", "team3", "member"],
    ["User5", "team4", "member"],
    ["User6", "team1", "member"],
    ["User6", "team2", "member"],
    ["User6", "team3", "member"],
    ["User6", "team4", "member"],
    ["User6", "team5", "member"],
    ["User7", "team1", "member"],
    ["User7", "team2", "member"],
    ["User7", "team3", "member"],
    ["User7", "team4", "member"],
    ["User7", "team5", "member"],
    ["User7", "team6", "member"],
    ["User8", "team1", "member"],
    ["User8", "team2", "member"],
    ["User8", "team4", "member"],
    ["User8", "team5", "member"],
    ["User8", "team6", "member"],
    ["User9", "team1", "member"],
    ["User9", "team2", "member"],
    ["User9", "team4", "member"],
    ["User9", "team5", "member"],
    ["User9", "team6", "member"],
    ["User10", "team1", "member"],
    ["User10", "team2", "member"],
    ["User10", "team4", "member"],
    ["User10", "team5", "member"],
    ["User10", "team6", "member"]
  ]
}

resource "github_team_membership" "memberships" {
  for_each = { for membership in local.memberships : "${membership[0]}-${membership[1]}" => membership }

  team_id = github_team[each.value[1]].id
  username = each.value[0]
  role = each.value[2]
}
