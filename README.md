# Dactyl-like custom split keyboard

This is firmware for a dactyl-like custom split keyboard I made with the [Cosmos](https://ryanis.cool/cosmos/beta#cm:CowBChESBRCQQSATEgIgABIAODFAAAoREgUQkE0gExICIAASADgdQAAKHxIFEJBZIBMSAiAAEgMQsC8SBRCwXyAoOAlAgOSG6AEKHRIFEJBlIBMSAiAAEgMQsDsSBRCwayAoOApAgIQ1ChUSBRCQcSATEgIgABIAOB5AgLqKkAIYAEDohaCu8FVI3PCioAEKaAoXEhMQwIACQICAmAJIwpmglZC8AVBDOAgKFRIQEEBAgIAgSNCVgN2Q9QNQC1CeAgoUEhAQQECAgPgBSOaZ/KeQC1BXUH8KA1CCAhgCIgoIyAEQyAEYACAAQMuL/J/QMUitkdyNwZMGCogBChESBRCQNSATEgIgABIAODJAAAoREgUQkCkgExICIAASADgeQAAKHBIFEJAdIBMSAiAAEgASBRCwXyAoOApAgKyHqAIKHBIFEJARIBMSAiAAEgASBRCwayAoOAlAgNiGqAIKFRIFEJAFIBMSAiAAEgA4HUCAvoewARgBQOeFoK7wVUjc7qKYAYIBAQJYSHjIg7Rs) keyboard generator.

## Config

Most of the config is in [boards/shields/custom_split](boards/shields/custom_split).

## Flashing procedure

Connect a half of the keyboard and put it into bootloader mode by double-tapping reset.

Then, to flash a settings reset:

```bash
python3 flash.py --reset
```

this pulls the latest firmware from GitHub and flashes it.

Then to flash a half of the keyboard:

```bash
python3 flash.py --left
python3 flash.py --right
```

