# Snort-Based Intrusion Detection System (IDS)

## CODTECH Internship Project

- **Project Number:** 14
- **Intern Name:** KAMANI SREEJA
- **Intern ID:** CITS9336
- **Internship Duration:** 6 WEEKS
- **Technology:** Snort 2.9.20, Npcap, Python, Scapy
- **Platform:** Windows 11

## 1. Project Overview

This project demonstrates a basic signature-based Intrusion Detection System (IDS) using Snort. A custom rule identifies a specified test string in TCP packet payloads and generates an alert when the pattern matches.

## 2. Objectives

- Install and verify Snort on Windows.
- Configure a custom Snort detection rule.
- Generate a synthetic packet capture for testing.
- Analyze the packet capture and verify the generated alert.

## 3. Technologies Used

- **Snort 2.9.20:** Network intrusion detection engine.
- **Npcap:** Windows packet-capture driver.
- **Python:** Test-capture generation.
- **Scapy:** Packet construction and PCAP writing.
- **Windows 11:** Development and testing environment.

## 4. Custom Detection Rule

File: `rules/local.rules`

```text
alert tcp any any -> any any (msg:"CODTECH IDS Test Pattern Detected"; content:"CODTECH-IDS-TEST"; sid:1000001; rev:1;)
```

The rule alerts when a TCP packet contains the string `CODTECH-IDS-TEST`. It is a demonstration signature, not a complete attack-detection rule.

## 5. Implementation and Testing

1. Installed Snort 2.9.20 and Npcap.
2. Verified the Snort executable and available network interfaces.
3. Created the custom detection rule.
4. Used Python and Scapy to generate a synthetic PCAP file containing the test string.
5. Ran Snort in offline PCAP-analysis mode with the custom rule.
6. Verified the alert in the command-line output.

### Test Result

- **Rules loaded:** 1
- **Packets processed:** 1
- **Alerts generated:** 1
- **Packets dropped:** 0
- **Observed alert:** `CODTECH IDS Test Pattern Detected`

Evidence is available in `screenshots/snort_detection_alert.png`.

## 6. Project Structure

```text
Snort-IDS/
├── rules/
│   └── local.rules
├── screenshots/
│   └── snort_detection_alert.png
├── logs/
├── create_test_pcap.py
├── test_capture.pcap
├── requirements.txt
├── .gitignore
└── README.md
```

## 7. How to Run the Test

Install the Python dependency:

```bash
python -m pip install -r requirements.txt
```

Generate the synthetic packet capture:

```bash
python create_test_pcap.py
```

Run Snort against the capture from the project directory:

```bat
"C:\Snort\bin\snort.exe" -r "test_capture.pcap" -c "rules\local.rules" -A console -N
```

A successful test should display `CODTECH IDS Test Pattern Detected`.

## 8. Limitations

- The validation uses a synthetic packet capture, not real malicious traffic.
- The custom rule detects only one specific test string.
- This test validates signature matching in offline PCAP analysis; it does not establish successful live network monitoring.
- The minimal configuration reports that no preprocessors are configured.
- No automatic blocking, incident response, or comprehensive attack classification is implemented.

## 9. Conclusion

The project demonstrates a working Snort signature rule and verifies that it generates an alert when the test payload matches. It provides a starting point for learning network traffic inspection and signature-based intrusion detection.

## Disclaimer

This project is intended for educational and authorized defensive-security testing only.