<template>
  <div class="admin-panel">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-3">
          <div class="sidebar">
            <ul class="nav flex-column">
              <li class="nav-item">
                <router-link to="/admin/dashboard" class="nav-link" active-class="active">
                  <i class="fa fa-home"></i> Dashboard
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/admin/orders" class="nav-link" active-class="active">
                  <i class="fa fa-shopping-cart"></i> Orders
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/admin/tables" class="nav-link" active-class="active">
                  <i class="fa fa-table"></i> Tables
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/admin/menus" class="nav-link" active-class="active">
                  <i class="fa fa-bars"></i> Menus
                </router-link>
              </li>
            </ul>
            <button class="logout-btn btn btn-danger" @click="logout">Logout</button>
          </div>
        </div>
        <div class="col-md-9">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.commit('removeToken');
      location.reload(true);
    }
  }
};
</script>

<style scoped>
.admin-panel {
  height: 100vh;
}

.sidebar {
  background-color: #f8f9fa;
  padding-top: 20px;
  padding-bottom: 20px;
}

.nav-link {
  color: #333;
}

.nav-link i {
  margin-right: 10px;
}

.nav-link:hover {
  background-color: #e9ecef;
}

.nav-link.active {
  background-color: #007bff;
  color: #fff;
}

.logout-btn {
  margin-top: auto;
  width: 100%;
  padding: 10px;
  cursor: pointer;
}

.logout-btn:hover {
  background-color: #c82333;
}
</style>