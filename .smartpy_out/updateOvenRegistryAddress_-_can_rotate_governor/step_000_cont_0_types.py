import smartpy as sp

tstorage = sp.TRecord(administrator = sp.TAddress, balances = sp.TBigMap(sp.TAddress, sp.TRecord(approvals = sp.TMap(sp.TAddress, sp.TNat), balance = sp.TNat).layout(("approvals", "balance"))), dexterAddress = sp.TAddress, governorAddress = sp.TAddress, metadata = sp.TBigMap(sp.TString, sp.TBytes), ovenRegistryAddress = sp.TAddress, paused = sp.TBool, rewardAmount = sp.TNat, savedState_depositor = sp.TOption(sp.TAddress), savedState_redeemer = sp.TOption(sp.TAddress), savedState_tokensToDeposit = sp.TOption(sp.TNat), savedState_tokensToRedeem = sp.TOption(sp.TNat), state = sp.TIntOrNat, tokenAddress = sp.TAddress, token_metadata = sp.TBigMap(sp.TNat, sp.TPair(sp.TNat, sp.TMap(sp.TString, sp.TBytes))), totalSupply = sp.TNat, underlyingBalance = sp.TNat).layout((((("administrator", "balances"), ("dexterAddress", "governorAddress")), (("metadata", "ovenRegistryAddress"), ("paused", "rewardAmount"))), ((("savedState_depositor", "savedState_redeemer"), ("savedState_tokensToDeposit", "savedState_tokensToRedeem")), (("state", "tokenAddress"), ("token_metadata", ("totalSupply", "underlyingBalance"))))))
tparameter = sp.TVariant(approve = sp.TRecord(spender = sp.TAddress, value = sp.TNat).layout(("spender", "value")), burn = sp.TRecord(address = sp.TAddress, value = sp.TNat).layout(("address", "value")), default = sp.TUnit, deposit = sp.TNat, deposit_callback = sp.TNat, getAdministrator = sp.TPair(sp.TUnit, sp.TContract(sp.TAddress)), getAllowance = sp.TPair(sp.TRecord(owner = sp.TAddress, spender = sp.TAddress).layout(("owner", "spender")), sp.TContract(sp.TNat)), getBalance = sp.TPair(sp.TAddress, sp.TContract(sp.TNat)), getTotalSupply = sp.TPair(sp.TUnit, sp.TContract(sp.TNat)), liquidate = sp.TAddress, mint = sp.TRecord(address = sp.TAddress, value = sp.TNat).layout(("address", "value")), redeem = sp.TNat, redeem_callback = sp.TNat, setAdministrator = sp.TAddress, setPause = sp.TBool, transfer = sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat).layout(("from_ as from", ("to_ as to", "value"))), updateBalance = sp.TUnit, updateBalance_callback = sp.TNat, updateContractMetadata = sp.TPair(sp.TString, sp.TBytes), updateDexterAddress = sp.TAddress, updateGovernorAddress = sp.TAddress, updateOvenRegistryAddress = sp.TAddress, updateRewardAmount = sp.TNat, updateTokenMetadata = sp.TPair(sp.TNat, sp.TMap(sp.TString, sp.TBytes))).layout((((("approve", ("burn", "default")), ("deposit", ("deposit_callback", "getAdministrator"))), (("getAllowance", ("getBalance", "getTotalSupply")), ("liquidate", ("mint", "redeem")))), ((("redeem_callback", ("setAdministrator", "setPause")), ("transfer", ("updateBalance", "updateBalance_callback"))), (("updateContractMetadata", ("updateDexterAddress", "updateGovernorAddress")), ("updateOvenRegistryAddress", ("updateRewardAmount", "updateTokenMetadata"))))))
tglobals = { }
tviews = { }
