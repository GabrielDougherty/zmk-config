# Dactyl-like custom split keyboard

This is firmware for a dactyl-like custom split keyboard I made with the [Cosmos](https://ryanis.cool/cosmos/beta#cm:CowBChESBRCQQSATEgIgABIAODFAAAoREgUQkE0gExICIAASADgdQAAKHxIFEJBZIBMSAiAAEgMQsC8SBRCwXyAoOAlAgOSG6AEKHRIFEJBlIBMSAiAAEgMQsDsSBRCwayAoOApAgIQ1ChUSBRCQcSATEgIgABIAOB5AgLqKkAIYAEDohaCu8FVI3PCioAEKaAoXEhMQwIACQICAmAJIwpmglZC8AVBDOAgKFRIQEEBAgIAgSNCVgN2Q9QNQC1CeAgoUEhAQQECAgPgBSOaZ/KeQC1BXUH8KA1CCAhgCIgoIyAEQyAEYACAAQMuL/J/QMUitkdyNwZMGCogBChESBRCQNSATEgIgABIAODJAAAoREgUQkCkgExICIAASADgeQAAKHBIFEJAdIBMSAiAAEgASBRCwXyAoOApAgKyHqAIKHBIFEJARIBMSAiAAEgASBRCwayAoOAlAgNiGqAIKFRIFEJAFIBMSAiAAEgA4HUCAvoewARgBQOeFoK7wVUjc7qKYAYIBAQJYSHjIg7Rs) keyboard generator.

## Microcontroller

I used these Nice! Nano clones: https://www.aliexpress.us/item/3256808840197195.html?spm=a2g0o.cart.0.0.17fb38daXylpJW&mp=1&pdp_npi=6%40dis%21USD%21USD+23.89%21USD+13.24%21%21USD+13.24%21%21%21%4021032f3717760434681303450e9b52%2112000047645063315%21ct%21US%217546085639%21%211%210%21&gatewayAdapt=glo2usa#nav-description


## Config

Most of the config is in [boards/shields/custom_split](boards/shields/custom_split).

## Flashing procedure

Connect a half of the keyboard and put it into bootloader mode by double-tapping reset.

Then, to flash a settings reset:

```bash
python3 flash.py --reset
```

this pulls the latest firmware from GitHub and flashes it.

Then to flash a half of the keyboard, put it back into bootloader mode and flash its respective side:

```bash
python3 flash.py --left
python3 flash.py --right
```

