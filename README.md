# Firewall Network Flood Mitigation Project

## Overview
This project monitors network traffic on two seperare Ubuntu VMs and automatically blocks IPs exceeding a threshold using UFW/iptables. It demonstrates baseline network behavior, flooding without a firewall, and the impact of the firewall script.

## Folder Structure
- `scripts/` – Python scripts used for flooding and firewall automation
- `baseline_logs/` – Displays network packet baseline, UFW baseline, iptables baseline, and conntrack baseline logs
- `flood_no_firewall_logs/` –  Displays network packets, UFW , iptables , and conntrack logs, following flood and prior to firewall script implementation
- `flood_with_firewall_logs/` – Displays network packets, UFW , iptables , and conntrack logs, following flood and after firewall script implementation
- `README.md` – Project description

## Dependencies
- Python 3
- Scapy
- UFW
- conntrack
- iptables

